# Stat Calculator

Enter your current stat allocation (starting stat) and the number you want to arrive at (ending stat).<br>
Click "Calculate" to show the cumulative amount of experience needed in order to achieve your stat goal.

<div style="margin-bottom: 10px;">
    <label for="startStat">Starting Stat (1-255):</label>
    <input type="number" id="startStat" min="1" max="255" required>
</div>
<div style="margin-bottom: 10px;">
    <label for="endStat">Ending Stat (1-255):</label>
    <input type="number" id="endStat" min="1" max="255" required>
</div>
<button onclick="calculateExperience()">Calculate</button>
<div id="result" style="margin-top: 10px;"></div>

<script>
    function calculateExperience() {
        const startStat = parseInt(document.getElementById('startStat').value);
        const endStat = parseInt(document.getElementById('endStat').value);
        let totalExperience = 0;

        if (startStat < 1 || startStat > 255 || endStat < 1 || endStat > 255 || startStat > endStat) {
            document.getElementById('result').innerText = "Please enter valid starting and ending stat values.";
            return;
        }

        for (let stat = startStat; stat < endStat; stat++) { // Use '<' to exclude endStat
            if (stat <= 29) {
                totalExperience += 3000000; // Fixed amount for stats 30 or lower
            } else {
                totalExperience += (stat * 75000 + 2000000); // Formula for stats 31 and above
            }
        }

        // Format the total experience with commas
        document.getElementById('result').innerText = `Total Experience Required: ${totalExperience.toLocaleString()}`;
    }
</script>
