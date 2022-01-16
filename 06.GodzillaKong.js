// 05. Godzilla vs. Kong
function godzillaKong(input) {
    const budget = Number(input[0]);
    const statistCount = Number(input[1]);
    const dressPrice = Number(input[2]);
    
    const stageCost = budget * 0.1;
    let dressCost = statistCount * dressPrice;
        
    if (statistCount > 150) {
        dressCost *= 0.9;
    }
    let totalCost = stageCost + dressCost;
    let difference = Math.abs(budget - totalCost);
    

    if (budget >= totalCost) {
        console.log('Action!');
        console.log(`Wingard starts filming with ${difference.toFixed(2)} leva left.`);
    } else {
        console.log('Not enough money!');
        console.log(`Wingard needs ${difference.toFixed(2)} leva more.`)
    }

}
