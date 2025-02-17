import { render } from "@testing-library/react";
import App from "../../App";

describe("App Component", () => {
  test("renders without crashing", () => {
    render(<App />);
    // This is a basic test to ensure the component renders
    expect(document.body).toBeTruthy();
  });
});
