{
  description = "TD INSA : introduction à ROS 2 Jazzy avec turtlesim";

  inputs.nix.url = "github:gepetto/nix";

  outputs =
    inputs:
    inputs.nix.lib.mkFlakoboros inputs (
      { lib, ... }:
      {
        # Jazzy uniquement (par défaut flakoboros évalue humble, jazzy, kilted, lyrical, rolling)
        rosDistros = [ "jazzy" ];
        rosShellDistro = "jazzy";

        extraRosPackages = [
          "ros-core"
          "turtlesim"
          "demo-nodes-py"
          "rqt-graph"
          "rqt-console"
          "ros2bag"
          "ros2launch"
        ];
      }
    );
}
