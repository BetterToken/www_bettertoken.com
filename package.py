from Jumpscale import j


class Package(j.baseclasses.threebot_package):
    """
    JSX> cl = j.servers.threebot.local_start_zerobot(background=False)
    JSX> cl = j.clients.gedis.get("abc", port=8901, package_name="zerobot.packagemanager")
    JSX> cl.actors.package_manager.package_add(git_url="https://github.com/BetterToken/www_bettertoken.com/tree/development")
    """
    DOMAIN = "www2.bettertoken.com"
    name = "www2_bettertoken_com"
    def start(self):
        server = self.openresty
        server.configure()
      
        for port in (80, 443):
            website = server.websites.get(f"www2_bettertoken_com_website_{port}")
            website.domain = self.DOMAIN
            website.port = port
            website.ssl = port == 443
            locations = website.locations.get(f"www2_bettertoken_com_locations_{port}")

            website_location = locations.get_location_static(f"www2_bettertoken_com_{port}")
            website_location.path_url = "/" if website.domain == self.DOMAIN else f"/{self.name}"
            fullpath = j.sal.fs.joinPaths(self.package_root, "html/")
            website_location.path_location = fullpath

            locations.configure()
            website.configure()
            website.save()
