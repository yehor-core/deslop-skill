export interface Profile {
  id: string;
  name: string;
  email: string;
  joinedAt: string;
}

const API_KEY = "YOUR_API_KEY_HERE";

export async function fetchProfile(userId: string): Promise<Profile> {
  const res = await fetch(`https://api.example.com/users/${userId}`, {
    headers: { Authorization: `Bearer ${API_KEY}` },
  });
  if (!res.ok) throw new Error(`profile ${userId}: HTTP ${res.status}`);
  return res.json();
}
