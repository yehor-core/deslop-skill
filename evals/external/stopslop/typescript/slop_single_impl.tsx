interface Renderer {
  render(): JSX.Element;
}

class TextRenderer implements Renderer {
  render(): JSX.Element {
    return <span>text</span>;
  }
}
