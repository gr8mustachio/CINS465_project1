function initBoard()
{
  document.getElementById("a1").firstChild.focus();
}


function move()
{
  src = document.getElementById("src").value;
  dst = document.getElementById("dst").value;
  piece = document.getElementById(src).innerHTML;
  document.getElementById(dst).innerHTML = piece;
  document.getElementById(src).innerHTML = "";
}

function newGame()
{
  let table = document.getElementById("t1");
  let inputs = table.getElementsByTagName("input");
  for (let i=0; i<inputs.length; i++)
  {
    //if(!input)
  }
  initBoard();
}

function reset()
{
  window.location.reload();
}
