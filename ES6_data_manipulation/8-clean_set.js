export default function cleanSet(set, startString) {
  let result = '';
  if (typeof startString === 'string' && startString) {
    for (const value of set) {
      if (value && typeof value === 'string' && value.startsWith(startString)) {
        const restOfValue = value.slice(startString.length);
        if (result) {
          result += `-${restOfValue}`;
        } else {
          result += restOfValue;
        }
      }
    }
  }
  return result;
}
