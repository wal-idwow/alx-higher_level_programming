#!/usr/bin/node

exports.esrever = function (list) {
  const reverselst = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverselst.push(list[i]);
  }
  return reverselst;
};
