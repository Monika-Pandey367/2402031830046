function convert() {
  let value = parseFloat(document.getElementById("value").value);
  let fromUnit = document.getElementById("from-unit").value;
  let toUnit = document.getElementById("to-unit").value;

  if (isNaN(value)) {
    document.getElementById("result").textContent = "Please enter a valid number.";
    return;
  }

  const conversionRates = {
    cm: { m: 0.01, km: 0.00001, inches: 0.393701, feet: 0.0328084 },
    m: { cm: 100, km: 0.001, inches: 39.3701, feet: 3.28084 },
    km: { cm: 100000, m: 1000, inches: 39370.1, feet: 3280.84 },
    inches: { cm: 2.54, m: 0.0254, km: 0.0000254, feet: 0.0833333 },
    feet: { cm: 30.48, m: 0.3048, km: 0.0003048, inches: 12 }
  };

  if (fromUnit === toUnit) {
    document.getElementById("result").textContent = "Units are the same, no conversion needed.";
    return;
  }

  let convertedValue = value * conversionRates[fromUnit][toUnit];
  document.getElementById("result").textContent = `${value} ${fromUnit} = ${convertedValue} ${toUnit}`;
}
