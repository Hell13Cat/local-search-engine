function adapt() {
    if(/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)){
        var ytvid = document.querySelector('#ytvid');
        var widthScreen = document.documentElement.clientWidth
        var widthVid = Math.round(widthScreen / 100 * 80) + "px";
        var heightVid = Math.round((widthScreen / 100 * 80) / 1280 * 720) + "px";
        ytvid.width = widthVid;
        ytvid.height = heightVid;
    }
  }