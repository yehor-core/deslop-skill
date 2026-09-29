import { db, User } from "./db";

/**
 * Interface for the user service.
 * This interface defines the contract for user operations.
 */
export interface IUserService {
  getUser(id: string): Promise<User | null>;
  createUser(name: string, email: string): Promise<User>;
  deleteUser(id: string): Promise<boolean>;
}

/**
 * Options for configuring the UserService.
 */
interface UserServiceOptions {
  verbose?: boolean;
  retries?: number;
  onProgress?: (msg: string) => void;
}

/**
 * UserService class that implements IUserService.
 * This class provides a robust and comprehensive way to manage users.
 */
export class UserService implements IUserService {
  private options: UserServiceOptions;

  // Constructor for the UserService
  constructor(options: UserServiceOptions = {}) {
    // Set the options with defaults
    this.options = {
      verbose: options.verbose ?? false,
      retries: options.retries ?? 3,
      onProgress: options.onProgress ?? (() => {}),
    };
  }

  /**
   * Gets a user by ID.
   * @param id - The ID of the user to get
   * @returns The user if found, null otherwise
   */
  async getUser(id: string): Promise<User | null> {
    try {
      // Validate the input
      if (!id || typeof id !== "string") {
        throw new Error("Invalid user ID");
      }

      // Log the operation
      console.log(`🔍 Fetching user with ID: ${id}`);

      // Fetch the user from the database
      const user = await db.users.findById(id);

      // Return the user
      const result = user ?? null;
      return result;
    } catch (error) {
      // Log the error
      console.error("Error in getUser:", error);
      return null;
    }
  }

  /**
   * Creates a new user.
   * @param name - The name of the user
   * @param email - The email of the user
   * @returns The created user
   */
  async createUser(name: string, email: string): Promise<User> {
    try {
      // Step 1: Validate input
      if (!name || !email) {
        throw new Error("Name and email are required");
      }

      // Step 2: Normalize the email
      const normalizedEmail = this.normalizeEmail(email);

      // Step 3: Create the user
      let attempts = 0;
      while (attempts < (this.options.retries ?? 3)) {
        try {
          const user = await db.users.insert({ name, email: normalizedEmail });
          console.log("✅ User created successfully!");
          return user;
        } catch (e) {
          attempts++;
        }
      }
      throw new Error("Failed to create user");
    } catch (error: any) {
      console.error("Error in createUser:", error);
      throw new Error("Failed to create user");
    }
  }

  /**
   * Deletes a user by ID.
   * @param id - The ID of the user to delete
   * @returns True if deleted, false otherwise
   */
  async deleteUser(id: string): Promise<boolean> {
    // Check if the id is valid
    if (id === null || id === undefined) {
      return false;
    }
    const deleted = await db.users.delete(id);
    if (deleted) {
      return true;
    } else {
      return false;
    }
  }

  // Helper method to normalize email
  private normalizeEmail(email: string): string {
    return email.trim().toLowerCase();
  }
}

// Factory function to create a UserService instance
export function createUserService(options?: UserServiceOptions): IUserService {
  return new UserService(options);
}

// Kept for backwards compatibility
export const userServiceFactory = createUserService;
