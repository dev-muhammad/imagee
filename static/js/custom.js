function readFile() {
  
    if (this.files && this.files[0]) {
      
      var FR = new FileReader();
      
      FR.addEventListener("load", function(e) {
        document.getElementById("preview").src = e.target.result;
        document.getElementById('uploadLabel').style.display = "none";
        document.getElementById('uploadedLabel').textContent = "File size: " + parseFloat(document.getElementById('file').files[0].size/1024).toFixed(2) + " kb";
        document.getElementById('actionArea').style.display = "block";
      }); 
      
      FR.readAsDataURL( this.files[0] );
    }
    
  }

function showOptimizedImage(imageBase64){
    // document.getElementById("optimized").src = imageBase64;
    document.getElementById("optimized").setAttribute('src', imageBase64);
    document.getElementById('resultBlock').style.display = "block";
}


async function postData(url = '') {
    let formData = new FormData();     
    formData.append("image", file.files[0]);
    const response = await fetch(url, {
        method: "POST", 
        body: formData
    });
    return response.json();
  }

function uploadFile() {
    btn = document.getElementById('optimize');
    btn.disabled = true;
    btn.classList.add("animate");
    btn.textContent = "Optimizing"
    postData('/image-optimize')
    .then(data => {
        var text = ""
        if (data.status == "success"){
            showOptimizedImage(data.image);
            if (data.original_size > data.optimized_size){
                text = "Optimized " + String(parseFloat(data.optimization_rate*100).toFixed(2)) + "%"
            }else{
                text = "Oops, can't optimize image :/"
            }
            text += "<br/><br/>New size: " + parseFloat(data.optimized_size/1024).toFixed(2) + " kb";
            document.getElementById("optimizedLabel").innerHTML = text
            document.getElementById('reset').style.display = "block";
            document.getElementById('optimize').classList.remove("animate")
            btn.textContent = "Optimized"
        }else{
            text = "Oops, can't optimize image:/"
            text += "<br/><br/>Please, try again :)"
            document.getElementById("uploadedLabel").innerHTML = text
            btn.textContent = "Optimization failed"
            document.getElementById("optimized").setAttribute('src',"")
            document.getElementById('reset').style.display = "block";
            document.getElementById('optimize').classList.remove("animate")
        }
    });
}

function downloadImage(){
    var a = document.createElement("a"); 
    a.href = document.getElementById("optimized").src
    a.download = "min_" + document.getElementById("file").files[0].name
    a.click();
}

function resetAll(){
    document.getElementById('resultBlock').style.display = "none";
    document.getElementById('actionArea').style.display = "none";
    document.getElementById('optimize').disabled = false;
    document.getElementById('reset').style.display = "none";
    document.getElementById("optimized").setAttribute('src',"")
    document.getElementById('optimize').textContent = "Optimize"
    document.getElementById('file').value = null;
}

document.getElementById("file").addEventListener("change", readFile);
document.getElementById("optimize").addEventListener("click", uploadFile);
document.getElementById("download").addEventListener("click", downloadImage);
document.getElementById("reset").addEventListener("click", resetAll);