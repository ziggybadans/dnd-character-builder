import "@testing-library/jest-dom";

// Polyfill for TextEncoder/TextDecoder
if (typeof TextEncoder === "undefined") {
  global.TextEncoder = require("util").TextEncoder;
  global.TextDecoder = require("util").TextDecoder;
}

// Add any global test setup here
beforeAll(() => {
  // Setup any test environment variables or global mocks
});

afterAll(() => {
  // Clean up any test environment variables or global mocks
});
