[:octicons-arrow-left-24: Back to Calculators](./overview.md)<br>

# Stat Calculator

This calculator will provide how much experience it will take to max your stats for each of the three progression types (Pre-Master, Master and Grandmaster).


<style>
  .stat-inputs label,
  .stat-inputs input {
    display: inline-block;
    width: 60px;
    margin-right: 10px;
  }
  .stat-inputs {
    margin-bottom: 1em;
  }
  #statCapDisplay {
    font-weight: bold;
    margin-left: 10px;
  }
  .breakdown-STR { color: #c0392b; }   /* Red */
  .breakdown-INT { color: #2980b9; }   /* Blue */
  .breakdown-WIS { color: #8e44ad; }   /* Purple */
  .breakdown-CON { color: #27ae60; }   /* Green */
  .breakdown-DEX { color: #f39c12; }   /* Orange */

  .breakdown-STR input {
    border: 2px solid #c0392b;
    color: #c0392b;          /* stat-colored text */
  }
  .breakdown-INT input {
    border: 2px solid #2980b9;
    color: #2980b9;
  }
  .breakdown-WIS input {
    border: 2px solid #8e44ad;
    color: #8e44ad;
  }
  .breakdown-CON input {
    border: 2px solid #27ae60;
    color: #27ae60;
  }
  .breakdown-DEX input {
    border: 2px solid #f39c12;
    color: #f39c12;
  }

  .stat-inputs input {
    padding: 4px;
    border-radius: 4px;
  }
</style>

<label for="classSelect">Class:</label>
<select id="classSelect">
  <option value="">-- Select --</option>
  <option value="Warrior">Warrior</option>
  <option value="Monk">Monk</option>
  <option value="Rogue">Rogue</option>
  <option value="Wizard">Wizard</option>
  <option value="Priest">Priest</option>
</select>
<span id="statCapDisplay"></span>

<div>
  Progression:
  <label><input type="radio" name="progression" value="Pre-Master" checked> Pre-Master</label>
  <label><input type="radio" name="progression" value="Master"> Master</label>
  <label><input type="radio" name="progression" value="Grandmaster"> Grandmaster</label>
</div>

### Current stats

Enter your current stats as seen in your character sheet.
<div class="stat-inputs">
  <span class="breakdown-STR">
    <label for="strInput">STR:</label>
    <input type="number" id="strInput" min="1" max="215" value="1">
  </span>
  <span class="breakdown-INT">
    <label for="intInput">INT:</label>
    <input type="number" id="intInput" min="1" max="215" value="1">
  </span>
  <span class="breakdown-WIS">
    <label for="wisInput">WIS:</label>
    <input type="number" id="wisInput" min="1" max="215" value="1">
  </span>
  <span class="breakdown-CON">
    <label for="conInput">CON:</label>
    <input type="number" id="conInput" min="1" max="215" value="1">
  </span>
  <span class="breakdown-DEX">
    <label for="dexInput">DEX:</label>
    <input type="number" id="dexInput" min="1" max="215" value="1">
  </span>
</div>

### (Optional) XP/hour rate

This will calculate how long it will take for you to reach the total experience needed. Leave blank to have this omitted.

<label for="xpRateInput">XP/hour (in Millions):</label>
<input type="number" id="xpRateInput" min="0" step="5" />

### (Optional) Current experience

Entering your current experience will subtract it from the total amount needed. Leave blank to ignore any subtractions.

<label for="currentExpInput" title="Optional: Enter how much XP you've already gained toward these stats. It will be subtracted from the total needed.">
  Current Experience:
</label>
<input type="number" id="currentExpInput" min="0" step="1000" />

<button onclick="calculateExperience()">Calculate</button>

<details id="resultSection">
  <summary id="result">Total Experience needed:</summary>
  <ul id="breakdown"></ul>
</details>

<script>
  const statCaps = {
    Warrior: {
      "Pre-Master":  { STR: 120, INT: 50,  WIS: 50,  CON: 50,  DEX: 100 },
      "Master":      { STR: 180, INT: 80,  WIS: 80,  CON: 120, DEX: 150 },
      "Grandmaster": { STR: 215, INT: 100, WIS: 100, CON: 150, DEX: 180 }
    },
    Monk: {
      "Pre-Master":  { STR: 100, INT: 50,  WIS: 50,  CON: 120, DEX: 80 },
      "Master":      { STR: 150, INT: 80,  WIS: 80,  CON: 180, DEX: 120 },
      "Grandmaster": { STR: 180, INT: 100, WIS: 100, CON: 215, DEX: 150 }
    },
    Rogue: {
      "Pre-Master":  { STR: 100, INT: 50,  WIS: 50,  CON: 80,  DEX: 120 },
      "Master":      { STR: 150, INT: 80,  WIS: 80,  CON: 120, DEX: 180 },
      "Grandmaster": { STR: 180, INT: 100, WIS: 100, CON: 150, DEX: 215 }
    },
    Wizard: {
      "Pre-Master":  { STR: 50,  INT: 120, WIS: 100, CON: 80,  DEX: 50 },
      "Master":      { STR: 80,  INT: 180, WIS: 150, CON: 120, DEX: 80 },
      "Grandmaster": { STR: 100, INT: 215, WIS: 180, CON: 150, DEX: 100 }
    },
    Priest: {
      "Pre-Master":  { STR: 50,  INT: 100, WIS: 120, CON: 80,  DEX: 50 },
      "Master":      { STR: 80,  INT: 150, WIS: 180, CON: 120, DEX: 80 },
      "Grandmaster": { STR: 100, INT: 180, WIS: 215, CON: 150, DEX: 100 }
    }
  };

  function experienceForStat(current, max) {
    let totalExp = 0;
    for (let i = current + 1; i <= max; i++) {
      if (i <= 29) {
        totalExp += 3000000;
      } else {
        totalExp += (i - 1) * 75000 + 2000000;
      }
    }
    return totalExp;
  }

  function isValidStat(value) {
    const num = Number(value);
    return Number.isInteger(num) && num >= 1 && num <= 215;
  }

  function resetStatInputs() {
    ['strInput', 'intInput', 'wisInput', 'conInput', 'dexInput'].forEach(id => {
      document.getElementById(id).value = 1;
    });
  }

  function updateStatCapDisplay() {
    const selectedClass = document.getElementById('classSelect').value;
    const progression = document.querySelector('input[name="progression"]:checked').value;
    const display = document.getElementById('statCapDisplay');

    if (selectedClass && statCaps[selectedClass]) {
      const caps = statCaps[selectedClass][progression];
      display.textContent = `MAX: ${caps.STR} / ${caps.INT} / ${caps.WIS} / ${caps.CON} / ${caps.DEX}`;
      resetStatInputs();
    } else {
      display.textContent = '';
    }
  }

  document.getElementById('classSelect').addEventListener('change', updateStatCapDisplay);
  document.querySelectorAll('input[name="progression"]').forEach(radio => {
    radio.addEventListener('change', updateStatCapDisplay);
  });

  function calculateExperience() {
    const selectedClass = document.getElementById('classSelect').value;
    const progression = document.querySelector('input[name="progression"]:checked').value;
    const caps = statCaps[selectedClass][progression];

    const inputs = {
      STR: document.getElementById('strInput').value,
      INT: document.getElementById('intInput').value,
      WIS: document.getElementById('wisInput').value,
      CON: document.getElementById('conInput').value,
      DEX: document.getElementById('dexInput').value
    };

    for (let stat in inputs) {
      if (!isValidStat(inputs[stat])) {
        alert(`Invalid input for ${stat}. Please enter an integer between 1 and 215.`);
        return;
      }
    }

    const currentStats = {
      STR: parseInt(inputs.STR),
      INT: parseInt(inputs.INT),
      WIS: parseInt(inputs.WIS),
      CON: parseInt(inputs.CON),
      DEX: parseInt(inputs.DEX)
    };

    let totalExp = 0;
    const breakdown = {};

    for (let stat in currentStats) {
      const xp = experienceForStat(currentStats[stat], caps[stat]);
      breakdown[stat] = xp;
      totalExp += xp;
    }

    const currentExpInput = document.getElementById('currentExpInput').value;
    const currentExp = parseInt(currentExpInput) || 0;
    const remainingExp = Math.max(totalExp - currentExp, 0);

    const result = document.getElementById('result');
    result.innerText = `Total Experience needed: ${remainingExp.toLocaleString()}`;
    document.getElementById('resultSection').open = true;

    const breakdownList = document.getElementById('breakdown');
    breakdownList.innerHTML = '';

    for (let stat in breakdown) {
      const li = document.createElement('li');
      li.textContent = `${stat}: ${breakdown[stat].toLocaleString()} XP`;
      li.classList.add(`breakdown-${stat}`);
      breakdownList.appendChild(li);
    }

    const xpRateInput = document.getElementById('xpRateInput').value;
    const xpRateMillions = parseFloat(xpRateInput);

    if (!isNaN(xpRateMillions) && xpRateMillions > 0) {
      const xpRate = xpRateMillions * 1_000_000;
      const hours = remainingExp / xpRate;
      const days = hours / 24;

      const timeLi = document.createElement('li');
      timeLi.textContent = `Estimated time at ${xpRateMillions.toLocaleString()} million XP/hour: ${hours.toFixed(1)} hours (~${days.toFixed(1)} days)`;
      breakdownList.appendChild(timeLi);
    }
  }
</script>
