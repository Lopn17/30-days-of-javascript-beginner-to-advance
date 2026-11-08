const blocksContainer = document.querySelector('.block-container');

function getRandomNum(min, max) {
    return Math.floor(Math.random() * (max - min+1)) + min;
}

let totalBlocks = 7;
let numRangeMin = 1;
let numRangeMax = 15;

let numArray = [];

let selectedBlock = null;

for (let i = 0; i < totalBlocks; i++) {

    const block = document.createElement('button');
    block.classList.add('block-num');
    let blockNum = getRandomNum(numRangeMin,numRangeMax);
    numArray.push(blockNum);
    blocksContainer.append(block);
    block.textContent = numArray[i];
    
    block.addEventListener("click", () => {

        if (selectedBlock === block) {
            selectedBlock.classList.remove('selected');
            selectedBlock = null;
            return;
        }

        if (selectedBlock !== null) {
            selectedBlock.classList.remove('selected');
        }

        block.classList.add("selected");
        selectedBlock = block;
        console.log(selectedBlock);

    });
    
}
console.log(numArray);
