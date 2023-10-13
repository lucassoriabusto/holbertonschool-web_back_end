export default function cleanSet(set, startString) {
  let result = '';
  for (const value of set) {
    if (value.startsWith(startString)) {
      const restOfValue = value.slice(startString.length);
      if (result) {
        result += '-' + restOfValue;
      } else {
        result += restOfValue;
      }
    }
  }
  return result;
}
