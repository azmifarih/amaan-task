data "alicloud_zones" "default" {
  available_resource_creation = "VSwitch"
}

resource "alicloud_vpc" "vpc" {
  vpc_name       = "vpc"
  cidr_block = "10.0.0.0/16"
}

resource "alicloud_vswitch" "zone-1a" {
  vpc_id            = alicloud_vpc.vpc.id
  cidr_block        = "10.0.1.0/24"
  zone_id           = data.alicloud_zones.default.zones[0].id
  vswitch_name      = "zone-1a"
}

resource "alicloud_vswitch" "zone-1b" {
  vpc_id            = alicloud_vpc.vpc.id
  cidr_block        = "10.0.2.0/24"
  zone_id           = data.alicloud_zones.default.zones[1].id
  vswitch_name      = "zone-1b"
}

resource "alicloud_security_group" "security-group-1" {
  name        = "security-group-1"
  description = "security-group-1"
  vpc_id      = alicloud_vpc.vpc.id
}

resource "alicloud_security_group_rule" "security-group-1-http" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "intranet"
  policy            = "accept"
  port_range        = "80/80"
  priority          = 1
  security_group_id = alicloud_security_group.security-group-1.id
  cidr_ip           = "0.0.0.0/0"
}
