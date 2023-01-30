import { People } from "./people.js";
import { Notes } from "./notes.js";
import { DebugForm } from "./debug.js";

function main() {
  new People();
  new Notes();
  const debug = new DebugForm();
  debug.showResponse("");
}

main();
