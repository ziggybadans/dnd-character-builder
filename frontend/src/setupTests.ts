import "@testing-library/jest-dom";

// Polyfill for TextEncoder/TextDecoder
if (typeof global.TextEncoder === "undefined") {
  global.TextEncoder = function TextEncoder() {
    return {
      encode: function encode(str: string): Uint8Array {
        const arr = new Uint8Array(str.length);
        for (let i = 0; i < str.length; i++) {
          arr[i] = str.charCodeAt(i);
        }
        return arr;
      },
    };
  } as any;
}

if (typeof global.TextDecoder === "undefined") {
  global.TextDecoder = function TextDecoder() {
    return {
      decode: function decode(arr: Uint8Array): string {
        return String.fromCharCode.apply(null, Array.from(arr));
      },
    };
  } as any;
}

// Add any global test setup here
beforeAll(() => {
  // Setup any test environment variables or global mocks
});

afterAll(() => {
  // Clean up any test environment variables or global mocks
});
