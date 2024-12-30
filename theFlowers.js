var e = document.getElementById('colors')
var f = document.getElementById('season')
const consoleImages = document.querySelectorAll(".collectionImage")
function changes() {
    var Evalue = e.value;
    var Fvalue = f.value;

    consoleImages.forEach((outfit)=> {
        if(Evalue == "allcolors" && Fvalue == "allseasons") {
            outfit.style.display = "inline-block"
            console.log(Evalue)
        } else {
           if ((outfit.classList.contains(Evalue) || Evalue == "allcolors") && (outfit.classList.contains(Fvalue) || Fvalue == "allseasons")){
            outfit.style.display = "inline-block"
            console.log(Evalue)
           } else {
            outfit.style.display = "none"
           }
        }
    })
    //return [Evalue, Svalue, Fvalue]
}

e.onchange = changes;
f.onchange = changes;
changes();

/*
consoleImages.forEach((outfit)=> {
    if(changes()[0] == "allcolors") {
        //outfit.style.display = "block"
        console.log(changes()[0])
    } else {
       if (outfit.classList.contains(changes()[0])){
        //outfit.style.display = "block"
        console.log(changes()[0])
       } else {
        outfit.style.display = "none"
       }
    }
})
*/