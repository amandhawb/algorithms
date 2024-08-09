// given an array of logs, determine which branch has the more quantity of files changed.
// example:
// logs = [
    // "switch branch1"
    // "push file1"
    // "push file2"
    // "push file1"
    // "switch main"
    // "switch branch2"
    // "push file1"
    // "push file2"
    // "push file3"
// ]
// response: branch2

function solution(files) {
    let currentBranch = null;
    const branches = new Map();

    function switchBranch(newBranch) {
        if(!branches.has(newBranch)) {
            branches.set(newBranch, new Set());
        }
    }

    function addFiles(file) {
        let curr = branches.get(currentBranch);
        branches.set(curr.add(file));
    }

    function findBiggerBranch(allBranches) {
        let branchSize = 0;
        let branchName = "";

        console.log(allBranches);
    }

    for(let i = 0; i < files.length; i++) {
        let command = files[i].split(" ")[0];
        let secondArg = files[i].split(" ")[1];
        if(command === "switch") {
            currentBranch = secondArg;
            switchBranch(secondArg);
        } else if(command === "push") {
            addFiles(secondArg);
        }
    }

    findBiggerBranch(branches)
    
}

let logs = ["switch branch1",
    "push file1",
    "push file2",
    "push file1",
    "switch main",
    "switch branch2",
    "push file1",
    "push file2",
    "push file3",
    "switch branch2"
]

console.log(solution(logs));