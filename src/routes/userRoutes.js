const express = require("express");
const app = express();
const router = express.Router();
const user = require("../userController/userController");

router.post("/postCoordinates", user.postCoordinates);

module.exports = router;
