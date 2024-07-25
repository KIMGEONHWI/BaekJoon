const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", function (line) {
  input.push(line);
  if (input.length === 3) {
    rl.close();
  }
});
//필요한 3줄의 입력을 모두 받으면 입력 인터페이스를 close

rl.on("close", function () {
  let N = +input[0];
  let nums = input[1].split(" ").map(Number);
  let op = input[2].split(" ").map(Number);

  let min = 1000000000;
  let max = -1000000000;

  function dfs(n, res) {
    if (n == N) {
      max = Math.max(max, res);
      min = Math.min(min, res);
      return;
    } // n이 N과 같으면 모든 숫자를 사용한 것이므로, max와 min을 갱신한다
    for (let i = 0; i < 4; i++) {
      if (op[i] > 0) {
        //사용할 수 있는 연산자가 있으면
        op[i]--;
        if (i == 0) dfs(n + 1, res + nums[n]);
        else if (i == 1) dfs(n + 1, res - nums[n]);
        else if (i == 2) dfs(n + 1, res * nums[n]);
        else if (i == 3) dfs(n + 1, parseInt(res / nums[n]));
        op[i]++;
      }
    }
  }

  dfs(1, nums[0]);

  if (max === -0) max = 0;
  if (min === -0) min = 0;

  console.log(max);
  console.log(min);
});
