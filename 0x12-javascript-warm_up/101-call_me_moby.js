#!/usr/bin/node
exports.callMeMoby = function (x, Function) {
  for (let i = 0; i < x; i++) {
    Function();
  }
};
