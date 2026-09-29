function Wrapper(id: string) {
  return Inner(id);
}

function Inner(id: string) {
  return <div>{id}</div>;
}
