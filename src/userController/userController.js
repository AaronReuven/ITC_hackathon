class UserController {
  async postCoordinates(req, res, error) {
    const { X, Y } = req.body;
    try {
      console.log({ X: X, Y: Y });
      res.send({ res: res });
    } catch {
      res.send({ error: error });
    }
    console.log(error);
  }
}
module.exports = new UserController();
