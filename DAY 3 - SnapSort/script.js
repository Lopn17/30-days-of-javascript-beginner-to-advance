const blocksContainer = document.querySelector('.block-container');
const checkButton = document.getElementById('checkButton');
const feedback = document.querySelector('.feedback-container');

function getRandomNum(min, max) {
    return Math.floor(Math.random() * (max - min+1)) + min;
}

function sortedArray(arr) {
    return arr.toSorted((a,b) => a - b);
}

let totalBlocks = 7;
let numRangeMin = 1;
let numRangeMax = 15;
let numArray = [];
let selectedIndex = null;

// 1. Inisialisasi data awal (hanya mengisi array, belum membuat elemen HTML)
for (let i = 0; i < totalBlocks; i++) {
    numArray.push(getRandomNum(numRangeMin, numRangeMax));
}

let sortedNumArray = sortedArray(numArray);

function renderBoard() {
    blocksContainer.innerHTML = '';

    numArray.forEach((num, i) => {
        const block = document.createElement('button');
        block.classList.add('block-num');
        block.textContent = num;

        // Jika indeks ini sedang dipilih, tambahkan class 'selected'
        if (selectedIndex === i) {
            block.classList.add('selected');
        }

        block.addEventListener('click', () =>{
            // Kasus 1: Mengklik blok yang sama (batalkan pilihan)
            if (selectedIndex === i) {
                selectedIndex = null;
                renderBoard(); // Render ulang untuk menghilangkan efek 'selected'
                return;
            }

            // Kasus 2: Belum ada blok yang dipilih (pilih blok ini)
            if (selectedIndex === null) {
                selectedIndex = i;
                renderBoard(); // Render ulang untuk menampilkan efek 'selected'
            }
            
            else {
                [numArray[selectedIndex],numArray[i]] = [numArray[i],numArray[selectedIndex]];
                selectedIndex = null;
                renderBoard();
            }
        });

        blocksContainer.append(block);
    });
    
}

function arrayMatch(arr1, arr2) {
    if (arr1.length !== arr2.length) return false;

    return arr1.every((value, index) => value === arr2[index]);
}



checkButton.addEventListener('click', ()=>{
    let filteredArr = sortedNumArray.filter((num, index) => num === numArray[index]); 

    feedback.className = 'feedback-container';
    if (arrayMatch(numArray, sortedNumArray)) {
        feedback.classList.add('correct');
        feedback.textContent = `BENAR!`;
    } else {
        feedback.classList.add('incorrect');
        feedback.textContent = `Belum benar: ${filteredArr.length}/${sortedNumArray.length} posisi tepat`;
    }
});


renderBoard();
