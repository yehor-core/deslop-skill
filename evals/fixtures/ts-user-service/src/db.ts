export interface User {
  id: string;
  name: string;
  email: string;
}

const rows = new Map<string, User>();
let nextId = 1;

export const db = {
  users: {
    async findById(id: string): Promise<User | undefined> {
      return rows.get(id);
    },
    async insert(data: Omit<User, "id">): Promise<User> {
      const user = { id: String(nextId++), ...data };
      rows.set(user.id, user);
      return user;
    },
    async delete(id: string): Promise<boolean> {
      return rows.delete(id);
    },
  },
};
