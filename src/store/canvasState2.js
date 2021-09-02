import { makeAutoObservable } from "mobx";

class CanvasState2 {
  canvas2 = null;
  socket = null;
  sessionid = null;
  undoList = [];
  redoList = [];
  username = "";

  constructor() {
    makeAutoObservable(this);
  }

  setSessionId(id) {
    this.sessionid = id;
  }
  setSocket(socket) {
    this.socket = socket;
  }

  setUsername(username) {
    this.username = username;
  }

  setCanvas(canvas2) {
    this.canvas2 = canvas2;
  }

  pushToUndo(data) {
    this.undoList.push(data);
  }

  pushToRedo(data) {
    this.redoList.push(data);
  }

  undo() {
    let ctx = this.canvas2.getContext("2d");
    if (this.undoList.length > 0) {
      let dataUrl = this.undoList.pop();
      this.redoList.push(this.canvas2.toDataURL());
      let img = new Image();
      img.src = dataUrl;
      img.onload = () => {
        ctx.clearRect(0, 0, this.canvas2.width, this.canvas2.height);
        ctx.drawImage(img, 0, 0, this.canvas2.width, this.canvas2.height);
      };
    } else {
      ctx.clearRect(0, 0, this.canvas2.width, this.canvas2.heigth);
    }
  }

  redo() {
    let ctx = this.canvas2.getContext("2d");
    if (this.redoList.length > 0) {
      let dataUrl = this.redoList.pop();
      this.undoList.push(this.canvas2.toDataURL());
      let img = new Image();
      img.src = dataUrl;
      img.onload = () => {
        ctx.clearRect(0, 0, this.canvas2.width, this.canvas2.height);
        ctx.drawImage(img, 0, 0, this.canvas2.width, this.canvas2.height);
      };
    }
  }
}

export default new CanvasState2();
