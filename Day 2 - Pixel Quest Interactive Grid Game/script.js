const boxesContainer = document.querySelector(".boxes-container");
const targetLocation = document.querySelector("#answer");
const targetCoreAns = document.querySelector("#targetCoreAns");
const devMode = document.querySelector("#devMode");
const scoreStats = document.querySelector("#scoreStats");
const highScoreStats = document.querySelector("#highScoreStats");
const restartBtn = document.querySelector("#restartBtn");

let boxesTotal = 20;

let targetCore = Math.floor(Math.random() * 20);


let isGameOver = false;

let score = 0;

let highScore = 0;

function renderBox() {
    scoreStats.textContent = score;
    boxesContainer.innerHTML = '';
    for (let i = 0; i < boxesTotal; i++) {
        targetLocation.textContent = targetCore;
        const box = document.createElement("div");
        box.classList.add("box");
        box.textContent = "?";
        boxesContainer.appendChild(box);
        
        box.dataset.number = i;
        let boxId = box.dataset.number;
        
        const numId = document.createElement("div");
        numId.classList.add("idBox", "hidden")
        numId.textContent = boxId;
        box.appendChild(numId);
        
        let deveMode = false;

        score = 200;
        
        box.addEventListener('click',() => {

            if (isGameOver){
                return
            }

            if (box.classList.contains("selected") || box.classList.contains("target-core")){
                return;
            }

            if (boxId == targetCore) {
                box.textContent = "⭐";
                box.classList.add("target-core");
                box.appendChild(numId);
                boxesContainer.classList.add("done");
                scoreStats.textContent = score;
                isGameOver = true;
                alert("Game is over, your score: "+score);
                if (highScore < score) {
                    highScore = score;
                    highScoreStats.textContent = highScore;
                }
            } else {
                box.textContent = "x";
                box.classList.add("selected");
                box.appendChild(numId);
                score = score - 10;
                scoreStats.textContent = score;
            }
        });

        devMode.addEventListener('dblclick',()=>{
            if (deveMode) {
                numId.classList.add("hidden");
                targetCoreAns.classList.add("hidden");
                deveMode = false;
            } else {
                numId.classList.remove("hidden");
                targetCoreAns.classList.remove("hidden");
                deveMode = true;
            }
        });

    }
}

renderBox();

restartBtn.addEventListener('click', () => {
    isGameOver = false;
    score = 0;
    targetCore = Math.floor(Math.random() * 20);
    renderBox()

})