const fs = require("fs");
const { resourceUsage } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const n = input[0].split(" ")[1];
// sort를 이용해서 정렬해주고
const list = input[1]
  .split(" ")
  .map((x) => +x)
  .sort((a, b) => b - a);
// 커트라인에 해당되는 (상 받는 사람 중 가장 낮은 점수) 점수를 출력한다.
console.log(list[n - 1]);
