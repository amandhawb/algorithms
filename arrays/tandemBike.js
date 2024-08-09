// A tandem bicycle is a bicycle that's operated by two people: person A and
// person B. Both people pedal the bicycle, but the person that pedals faster
// dictates the speed of the bicycle. So if person A pedals at a speed of 5,
// and person B pedals at a speed of 4, the tandem bicycle moves at a speed 5. (https://www.algoexpert.io/questions/tandem-bicycle)

function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, faster) {
    if(!faster) {
        redShirtSpeeds.sort((a,b) => b -a );
    } else {
        redShirtSpeeds.sort((a,b) => a - b);
    }

    blueShirtSpeeds.sort((a,b) => a-b);

    let totalSpeed = 0;

    for(let i = 0; i < redShirtSpeeds.length; i++ ) {
        let rider1 = redShirtSpeeds[i];
        let rider2 = blueShirtSpeeds[blueShirtSpeeds.length -i -1];
        totalSpeed += Math.max(rider1, rider2);
    }

    return totalSpeed;
}

console.log(tandemBicycle([5,5,3,9,2], [3,6,7,2,1], true));
