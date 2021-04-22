Deliverables
------------

There are 4 deliverables that should come in the form of this git repository (either zipped and sent to us,
or made available as a `clone`-able repository):

1. Specification of whether your solution requires a clean install of Ubuntu 18.04 or Mac OS.
2. A script, named `setup`, that installs any dependencies and sets up the system for your submission.  It should be in the
   top level directory and be runnable via `./setup`.
3. A script, named `build`, that carries out any build steps your solution requires. It should be in the top level directory
   and runnable via `./build`.
4. A `gRPC` server that implements the `NLImageService` interface, provides `--port` and `--host` and
   is runnable via `./server --port <...> --host <...>` in the top level directory of your submission (it's okay
    if the `./server` executable just wraps a build artifact)
5. A client that provides `--port`, `--host`, `--input`, `--output`, `--rotate`, and `--mean` arguments and can be
   run from the top level directory of your submission via
   `./client --port <...> --host <...> --input <...> --output <...> --rotate <...> --mean` (it's okay if the `./client`
   executable just wraps a build artifact)
6. Discussion of limitations or known issues with your solution, how you'd change it for production given more time and
   resources, and any other thoughts you have about the problem, your solution, or the tools you used.

