'use strict';

let rows = []

console.log("IT WORK")

for (let i = 0; i < 5; i++) {
  let row = [];
  for (let j = 0; j < 6; j++) {
    row.push([i, j]);
  };
  rows.push(row);
};

const RENDBOXES = rows.map(row => (
  <div key={row[0]}>
    {row.map(item => (
    <input type="checkbox" key={item}></input>))}
  </div>));

var App = function() {
  console.log("running")
  return (
  <div>
    <p>Fretbox:</p>
    {RENDBOXES}
  </div>

  );
};

ReactDOM.render(
  <App />,
  document.getElementById('fretboxes')
);
