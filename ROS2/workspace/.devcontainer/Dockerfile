FROM ros:kilted-ros-core-noble

ENV ROS_DISTRO=kilted
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

ARG USERNAME=USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN if id -u $USER_UID ; then userdel `id -un $USER_UID` ; fi

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip
ENV SHELL /bin/bash


WORKDIR /workspace

#COPY ./ROS2/workspace /workspace

RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build --symlink-install

USER $USERNAME
CMD ["/bin/bash"]