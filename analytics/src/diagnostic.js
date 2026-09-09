import { exec } from "node:child_process";

export const runHostDiagnostic = (host) => {
  return new Promise((resolve, reject) => {
    const command = "ping -c 1 " + host;

    exec(command, (error, stdout, stderr) => {
      if (error) {
        resolve({ success: false, error: stderr || error.message });
      } else {
        resolve({ success: true, output: stdout });
      }
    });
  });
};
