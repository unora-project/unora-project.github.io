# HP/MP

Calculate how much experience is needed to get to your destination base. Start by entering your starting base and then your ending base. If entering both HP and MP, it will give you the cumulative amount of experience for both.<br>
<br>
In Unora:

- HP is added in increments of 50, so your ending base must be in increments of 50 from your starting base<br>
- MP is added in increments of 25, so your ending base must be in increments of 25 from your starting base<bR>

| Attribute | Increments | Starting Base | Ending Base |
| :-------: | :--------: | :-----------: | :---------: |
| HP | +50 | <input type="number" id="startHP" min="0" step="50" required> | <input type="number" id="endHP" min="0" step="50" required>
| MP | +25 | <input type="number" id="startMP" min="0" step="25" required> | <input type="number" id="endMP" min="0" step="25" required>

<button onclick="calculateExperience()">Calculate</button>

<div class="result" id="result"></div>

<script>
    function formatNumber(num) {
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    function calculateExperience() {
        const startHP = parseInt(document.getElementById('startHP').value);
        const endHP = parseInt(document.getElementById('endHP').value);
        const startMP = parseInt(document.getElementById('startMP').value);
        const endMP = parseInt(document.getElementById('endMP').value);

        let totalExperienceNeeded = 0;
        let isValid = true;
        let resultMessage = '';

        // Calculate HP Experience
        if (!isNaN(startHP) && !isNaN(endHP) && startHP < endHP) {
            const hpDifference = endHP - startHP;

            // Check if the difference is a multiple of 50
            if (hpDifference % 50 !== 0) {
                resultMessage += "For HP: Please add increments of 50.\n";
                isValid = false;
            } else {
                const i = hpDifference / 50;
                for (let step = 1; step <= i; step++) {
                    const currentHP = startHP + 50 * step;
                    totalExperienceNeeded += currentHP * 500;
                }
            }
        }

        // Calculate MP Experience
        if (!isNaN(startMP) && !isNaN(endMP) && startMP < endMP) {
            const mpDifference = endMP - startMP;

            // Check if the difference is a multiple of 25
            if (mpDifference % 25 !== 0) {
                resultMessage += "For MP: Please add increments of 25.\n";
                isValid = false;
            } else {
                const j = mpDifference / 25;
                for (let step = 1; step <= j; step++) {
                    const currentMP = startMP + 25 * step;
                    totalExperienceNeeded += currentMP * 500;
                }
            }
        }

        // Display results
        if (!isValid) {
            document.getElementById('result').innerText = resultMessage.trim();
        } else {
            document.getElementById('result').innerText = `Total experience needed: ${formatNumber(totalExperienceNeeded)}`;
        }
    }
</script>
