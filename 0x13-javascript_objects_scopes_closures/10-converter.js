#!/usr/bin/node

exports.converter = function (base) {
  function toconvert (nb) {
    return nb.toString(base);
  }
  return toconvert;
};
