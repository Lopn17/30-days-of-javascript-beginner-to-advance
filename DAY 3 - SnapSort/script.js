const blocksContainer = document.querySelector('.block-container');

function getRandomNum(min, max) {
    return Math.floor(Math.random() * (max - min+1)) + min;
}

let totalBlocks = 7;
let numRangeMin = 1;
let numRangeMax = 15;

let numArray = [];

for (let i = 0; i < totalBlocks; i++) {

    const block = document.createElement('button');
    block.classList.add('block-num');
    let blockNum = getRandomNum(numRangeMin,numRangeMax);
    numArray.push(blockNum);
    blocksContainer.append(block);
    block.textContent = numArray[i];
    
    
}
console.log(numArray);
