# Environnement ROS 2 Jazzy (INSA, 4A)

Environnement Nix pour les TD ROS 2 Jazzy. Fournit `ros2`, `colcon`,
`turtlesim`, `rqt_graph`, `rqt_console`, `ros2 bag` et `ros2 launch`.

## Utilisation

```bash
git clone https://github.com/clementPene/INSA_ros2_env
cd INSA_ros2_env
direnv allow
```

Le premier `direnv allow` télécharge l'environnement (compter plusieurs
minutes selon le réseau). Une fois dedans :

```bash
echo $ROS_DISTRO              # -> jazzy
ros2 pkg executables turtlesim
ros2 run turtlesim turtlesim_node
```

## Variables déjà réglées (`.envrc`)

- `ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST` et `ROS_DOMAIN_ID=11` :
  limitent la découverte des nodes à cette machine, pour ne pas voir
  ceux des autres postes de la salle.
- Avec [direnv](https://direnv.net/) installé et activé, elles sont
  exportées automatiquement en entrant dans le dossier
  (`direnv allow`).

## Code source de turtlesim

```bash
git clone -b jazzy https://github.com/ros/ros_tutorials.git src/ros_tutorials
```

## Espace de travail personnel

Ce dépôt sert aussi de workspace ROS 2 : les paquets que vous créez
avec `ros2 pkg create` vont dans `src/`, à la racine du dépôt.

```bash
mkdir src
cd src
ros2 pkg create --build-type ament_python --license Apache-2.0 mon_paquet
cd ..
colcon build --packages-select mon_paquet
```

`build/`, `install/` et `log/` (créés par `colcon build`) sont déjà
ignorés par `.gitignore` : pas de risque de les committer par erreur.
