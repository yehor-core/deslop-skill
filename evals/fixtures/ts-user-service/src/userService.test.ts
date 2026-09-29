import { describe, it, expect, vi } from "vitest";
import { UserService, createUserService } from "./userService";
import { db } from "./db";

describe("UserService", () => {
  describe("constructor", () => {
    it("should be defined", () => {
      expect(UserService).toBeDefined();
    });
  });

  describe("createUserService", () => {
    it("should return an instance", () => {
      const service = createUserService();
      expect(service).toBeTruthy();
    });
  });

  describe("getUser", () => {
    it("should call db.users.findById", async () => {
      const spy = vi.spyOn(db.users, "findById");
      const service = new UserService();
      await service.getUser("1");
      expect(spy).toHaveBeenCalledWith("1");
    });
  });

  describe("createUser", () => {
    it("creates a user with a normalized email", async () => {
      const service = new UserService();
      const user = await service.createUser("Ann", "  Ann@Example.COM ");
      expect(user.email).toBe("ann@example.com");
    });
  });
});
