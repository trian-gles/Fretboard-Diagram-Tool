'use strict';

let rows = []

for (let i = 0; i < 5; i++) {
  let row = [];
  for (let j = 0; j < 6; j++) {
    row.push([j, i]);
  };
  rows.push(row);
};

const RENDBOXES = rows.map(row => (
  <div key={row[0]}>
    {row.map(item => (
    <input type="checkbox" name={item} key={item} id="fret"></input>))}
  </div>));

var App = function() {
  console.log("doest this change?")
  return (
    <form action='/' method="POST">
      {RENDBOXES}
      <input type="submit"></input>
    </form>

  );
};

ReactDOM.render(
  <App />,
  document.getElementById('fretboxes')
);
