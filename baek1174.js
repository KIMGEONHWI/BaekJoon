const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = +input[0];
const arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; // 숫자는 반드시 줄어들어야 한다.
const visited = new Array(10).fill(false);
const result = [];
const answer = [];

for (let i = 1; i <= 10; i++) {
  dfs(0, 0, i);
}

answer.sort((a, b) => a - b);

console.log(answer[N - 1] ?? -1);

function dfs(start, idx, len) {
  if (idx === len) {
    let cand = 0;

    for (const num of result) {
      cand *= 10;
      cand += num;
    }

    answer.push(cand);
    return;
  }

  // 조합 알고리즘
  for (let i = start; i < 10; i++) {
    if (visited[i]) continue;

    visited[i] = true;
    result.push(arr[i]);
    dfs(i + 1, idx + 1, len);
    result.pop();
    visited[i] = false;
  }
}
