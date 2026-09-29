interface Props {
  label: string;
}

function loadRaw(): unknown {
  return {};
}

const data = loadRaw();
const p = data as any;

const raw = loadRaw();
const props = raw as unknown as Props;

// @ts-ignore
export function Widget() {
  return <div>{props.label}</div>;
}
