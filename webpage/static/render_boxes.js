'use strict';



let rows = []

for (let i = 0; i < 5; i++) {
  let row = [];
  for (let j = 0; j < 6; j++) {
    row.push([j, i]);
  };
  rows.push(row);
};

function Box(props) {
  let num = props.num
  return (rows.map(row => (
  <div key={row[0]}>
    <input type="text" class="fret_label" name={[num, row[0]]}></input>
    {row.map(item => (
    <input type="checkbox" name={[num].concat(item)} key={item} id="fret"></input>))}
  </div>)))
}

const BOXES = [0, 1, 2, 3, 4, 5, 6, 7, 8].map(num => (
  <div class="fretbox">
    <input type="text" class="box_title" name={num}></input>
    <Box num={num}/>
  </div>
));

var App = function() {
  return (
    <form action='/' method="POST">
        <div id="all_boxes">
          {BOXES}
        </div>
      <div id="submit-div">
        <input type="submit"></input>
      </div>
    </form>
  );
};

ReactDOM.render(
  <App />,
  document.getElementById('fretboxes')
);
