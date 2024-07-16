let team1Points = 0;
let team2Points = 0;

function addToTeam(team) {
  if (team === 'team1') {
    team1Points++;
  } else if (team === 'team2') {
    team2Points++;
  }
  updatePointsLabel();
}

function updatePointsLabel() {
  const team1Name = document.getElementById('team1').value || 'Team 1';
  const team2Name = document.getElementById('team2').value || 'Team 2';
  const pointsLabel = document.getElementById('points-label');
  pointsLabel.textContent = `${team1Name} has ${team1Points} points. ${team2Name} has ${team2Points} points.`;
}