'use strict';



let rows = []

for (let i = 0; i < 5; i++) {
  let row = [];
  for (let j = 0; j < 6; j++) {
    row.push([j, i]);
  };
  rows.push(row);
};

const BOX = rows.map(row => (
  <div key={row[0]}>
    {row.map(item => (
    <input type="checkbox" name={item} key={item} id="fret"></input>))}
  </div>));

const BOXES = [0, 1, 2, 3, 4, 5].map(num => (
  <div class="fretbox">{BOX}</div>
));

  var App = function() {
    return (
      <form action='/' method="POST">
        {BOXES}
        <input type="submit"></input>
      </form>
    );
  };

ReactDOM.render(
  <App />,
  document.getElementById('fretboxes')
);
