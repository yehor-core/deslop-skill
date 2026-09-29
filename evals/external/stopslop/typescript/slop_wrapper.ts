function getUser(id: string) {
  return fetchUser(id);
}

const getUserArrow = (id: string) => fetchUser(id);

function fetchUser(id: string) {
  return { id, name: 'Alice' };
}
