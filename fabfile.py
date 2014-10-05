from fabric.api import local, run, env, put
env.graceful = False

env.user = 'mushfiq'
env.site_root = '/var/www/news'

def server():

    # env.serverpath = ''

    # env.password = '' #ssh password for user 
    # env.key_filename = ''# specify server public key
    #lis of hossts in env.hosts
    env.hosts      = [
    'shironambd.com',
    ]
    
    env.graceful = False

 
#sample method for git pull
def pull(branch_name):
	env.site_root = 'your_project_path'
	run('cd %s && git pull origin %s' % (env.site_root, branch_name))
 
#deploy current directories all code without fabfile.py	
def deploy():
	env.files = '*'
	env.site_name = 'shironambd'
	env.site_path    = '/var/www/news'
	run('sudo rm -rf %s/%s' % (env.site_path,env.site_name))
	local('zip -r %s.zip -x=fabfile.py %s' % (env.site_name, env.files))
	put('%s.zip' % env.site_name, env.site_root, use_sudo=True)
	run('cd  %s && sudo unzip %s.zip -d %s && sudo rm %s.zip' % (env.site_root, \
	env.site_name, env.site_name, env.site_name))
	local('rm -rf %s.zip' % env.site_name)
	
	
#restart apache of remote host
def restart_apache():
    cmd = "/usr/local/apache2/bin/apachectl -k graceful" if (env.graceful is True) \
          else "service httpd restart"
    run(cmd)
 
def latest_access_log():
	cmd = "sudo tail -n 10 /var/log/apache2/access.log"
	run(cmd)
	
def latest_error_log():
	cmd = "sudo tail -n 10 /var/log/apache2/error.log"
	run(cmd)
	
def clone():
	git_path = "git@github.com:mushfiq/shironambd.git"
	run('cd /var/www/testFab && git clone %s' % git_path)
