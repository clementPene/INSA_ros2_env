# Environnement ROS 2 Jazzy (INSA, 4A)

Environnement Nix pour les TD ROS 2 Jazzy. Fournit `ros2`, `colcon`,
`turtlesim`, `rqt_graph`, `rqt_console`, `ros2 bag` et `ros2 launch`.

## Utilisation

```bash
git clone https://github.com/clementPene/INSA_ros2_env
cd INSA_ros2_env
nix develop
```

Le premier `nix develop` télécharge l'environnement (compter plusieurs
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
  (`direnv allow`). Sinon, elles sont déjà héritées par `nix develop`
  si le shell qui l'a lancé les a chargées (ex. via `source .envrc`).

## Espace de travail personnel

Ce dépôt ne contient que l'environnement. Créez votre propre espace de
travail ROS 2 ailleurs, par exemple :

```bash
mkdir src/
```

Les paquets que vous créerez avec `ros2 pkg create` doivent aller dans
`/src`.
