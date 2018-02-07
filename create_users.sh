for i in {1..20}; do
  username="user$i";
  echo $username;
  useradd $username;
  echo "$username:jupyter*" | chpasswd;
  cp -r /home/ubuntu/exercises /home/$username/
  chown -R $username:$username /home/$username/exercises
done
