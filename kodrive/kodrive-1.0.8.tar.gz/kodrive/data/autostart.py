
def getSyncthingService():
  return '\n'.join([
    "[Unit]",
    "Description=Syncthing - Open Source Continuous File Synchronization for %I",
    "Documentation=man:syncthing(1)",
    "After=network.target"
    "Wants=syncthing-inotify@.service",
    "",
    "[Service]",
    "User=%i",
    "ExecStart=/usr/bin/syncthing -no-browser -no-restart -logflags=0",
    "Restart=on-failure",
    "SuccessExitStatus=3 4",
    "RestartForceExitStatus=3 4",
    "",
    "[Install]",
    "WantedBy=multi-user.target"
  ])
